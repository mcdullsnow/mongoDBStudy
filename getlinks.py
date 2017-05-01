#获取网页上的所有链接
import urllib.request
def get_all_links(url_content,page):
    while url_content != None:
        get_link(page)



#查找页面中的链接
def get_link(page):
    start_link = page.find("<a href=")
    if start_link == -1:
        return None,None
    else:
        start_pos = page.find('"',start_link)
        end_pos = page.find('"',start_pos+1)
        url_content = page[start_pos+1:end_pos]
        page = page[end_pos:]
        return url_content,page

#从网页获取内容，并转换为一个字符串
def get_page(url):
    page = urllib.request.urlopen(url)
    return str(page)

get_all_links(get_page("http://blog.csdn.net/fly_yr/article/details/51525945"))