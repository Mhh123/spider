



#GET /home HTTP/1.1
{
'Host': 'www.renren.com',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': 'ick_login=ad45689c-cf1d-4efa-a180-77f582a76fde; anonymid=jk0gqq8e-imjv31; depovince=GW; _r01_=1; JSESSIONID=abcKI_jDne8cE7hArgptw; jebe_key=94d9a879-e473-48cf-ab68-65d3aff55c19%7C24b3d26b79ad6218bede6cd1942ce9e9%7C1532482922946%7C1%7C1532482928665; wp_fold=0; BAIDU_SSP_lcr=https://www.baidu.com/link?url=-OYKJOIkDLaLLW589YQXfVIob_i5LglCSpimboybaYe&wd=&eqid=87abad1a00003d64000000025b57d548; _ga=GA1.2.420753870.1532483392; _gid=GA1.2.1790508705.1532483392; _de=2712953DB281699F7D49636C5D3D4B7E696BF75400CE19CC; t=695788f685945cb09ba6c70ac761c1251; societyguester=695788f685945cb09ba6c70ac761c1251; id=967106461; xnsid=30c21de2; jebecookies=82f8467b-03b7-4a79-a214-36c65caabeca|||||',
 }

#正则替换掉headers
# ctrl+r
# (.*): (.*)\n
# '$1': '$2'\n