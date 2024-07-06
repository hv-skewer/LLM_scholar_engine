import requests
from bs4 import BeautifulSoup
import os

def download_pdf(url, save_path):
    """
    下载指定URL的PDF文件到指定路径。
    
    参数:
    url (str): PDF文件的URL地址。
    save_path (str): 保存PDF文件的本地路径。
    """
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
            print(f"文件已保存至: {save_path}")
    else:
        print("下载失败，状态码：", response.status_code)

def fetch_pdf_links_from_page(url):
    """
    从给定的网页URL中提取所有PDF链接。
    
    参数:
    url (str): 包含PDF链接的网页地址。
    
    返回值:
    list: PDF链接列表。
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_links = [link.get('href') for link in soup.find_all('a', href=True) if link.get('href').endswith('.pdf')]
    return pdf_links

if __name__ == "__main__":
    # 示例网页URL，请替换为合法且允许爬取的网页地址
    example_url = "http://example.com/pdfs"
    
    # 获取PDF链接
    pdf_links = fetch_pdf_links_from_page(example_url)
    
    # 设置保存目录
    save_directory = "./downloaded_pdfs"
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    
    # 下载PDF文件
    for idx, link in enumerate(pdf_links):
        file_name = f"file_{idx}.pdf"
        full_path = os.path.join(save_directory, file_name)
        download_pdf(link, full_path)