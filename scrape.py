import os
import requests
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
import shutil

# Import the gallery_images array from dashboard.py
gallery_images = [
        "https://instagram.fdvo1-2.fna.fbcdn.net/v/t51.29350-15/454604646_466640676209155_3380286613199548365_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.fdvo1-2.fna.fbcdn.net&_nc_cat=107&_nc_ohc=YW8JlDqqxtcQ7kNvgFU5iBY&edm=AEhyXUkBAAAA&ccb=7-5&ig_cache_key=MzQzMDc2Nzg4MDk1NzU4OTg1NA%3D%3D.2-ccb7-5&oh=00_AYArSrLXD-0JS3hOqfOUrvtejUXjtddsUIaUPDcsLiAHAQ&oe=66D9D70D&_nc_sid=8f1549",
        "https://instagram.fdvo1-1.fna.fbcdn.net/v/t51.29350-15/451967798_1627282591179646_1347990780687164828_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.fdvo1-1.fna.fbcdn.net&_nc_cat=110&_nc_ohc=xeAA79UoDMQQ7kNvgH790DM&edm=AEhyXUkBAAAA&ccb=7-5&ig_cache_key=MzQxNTUzNTQ1NTMzMTQ4MzI0NQ%3D%3D.2-ccb7-5&oh=00_AYAb7iYh6X85IcgSmQZHHoFCgbN5RmK6v4ob3S1-_v9nCw&oe=66D9C86A&_nc_sid=8f1549",
        "https://instagram.fdvo1-1.fna.fbcdn.net/v/t51.29350-15/451949100_281147301728873_4344535088966241430_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.fdvo1-1.fna.fbcdn.net&_nc_cat=105&_nc_ohc=lZNf_8u-IH4Q7kNvgEbPI2g&edm=AEhyXUkBAAAA&ccb=7-5&ig_cache_key=MzQxNDgxMDY1MTA3MDY0OTQ2NQ%3D%3D.2-ccb7-5&oh=00_AYB-3mx1lFLiRLYTPuu6NZABhoWSm8D6U42nZBe2QaaeOw&oe=66D9D4AB&_nc_sid=8f1549",
        "https://instagram.fdvo1-1.fna.fbcdn.net/v/t51.29350-15/451568231_784378980526199_8206988422907434262_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.fdvo1-1.fna.fbcdn.net&_nc_cat=111&_nc_ohc=8NyuNSUU3wcQ7kNvgHEi3ZL&edm=AEhyXUkBAAAA&ccb=7-5&ig_cache_key=MzQxNDEwMzcxMTI3MzMxMTQyMA%3D%3D.2-ccb7-5&oh=00_AYAZmsfmGf8_Q_yag8AbtODyoFv93hvTsQK-f8U4qDJQ7g&oe=66D9D46C&_nc_sid=8f1549",
        "https://instagram.fdvo1-2.fna.fbcdn.net/v/t51.29350-15/451422861_807167024878922_6563196959970394039_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.fdvo1-2.fna.fbcdn.net&_nc_cat=102&_nc_ohc=JDrDvlqvTEoQ7kNvgEdAN5z&edm=AEhyXUkBAAAA&ccb=7-5&ig_cache_key=MzQxMzg5MzAyODYyMzUzMDU2MA%3D%3D.2-ccb7-5&oh=00_AYCN2SQi4L6BI28bjDvr_TFD9iXHwrvH28xMXGUi6bDE8w&oe=66D9CD60&_nc_sid=8f1549",
        "https://instagram.fdvo1-1.fna.fbcdn.net/v/t51.29350-15/451325297_1147953409821875_4506265271032796363_n.jpg?stp=dst-jpg_e15&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi44Mjh4MTQ3Mi5zZHIuZjI5MzUwLmRlZmF1bHRfY292ZXJfZnJhbWUifQ&_nc_ht=instagram.fdvo1-1.fna.fbcdn.net&_nc_cat=111&_nc_ohc=ZgIBE6Hsjg0Q7kNvgHhpIBJ&_nc_gid=ba002c1e32b74bacbc4b60503ef438e9&edm=AEhyXUkBAAAA&ccb=7-5&ig_cache_key=MzM3NTczMjI4MTYzNzAxMTUwMzc1NzEzMjI2ODI5Nzc0NjQ%3D.2-ccb7-5&oh=00_AYBCIqTrSxARvTG9FvMzH58JeTcoKZ5vdm0LcZ3y87BEmw&oe=66D9B9B8&_nc_sid=8f1549",
        "https://instagram.fdvo1-2.fna.fbcdn.net/v/t51.29350-15/444908646_2427124247488704_8617607920206163645_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.fdvo1-2.fna.fbcdn.net&_nc_cat=100&_nc_ohc=HQ_F7465WSAQ7kNvgGf-qmt&edm=AEhyXUkBAAAA&ccb=7-5&ig_cache_key=MzM3MDM2NzA1MjE5NTMyNDE1MA%3D%3D.2-ccb7-5&oh=00_AYAcqKSn4-eP7Im2OBD1XJHJHzuzIb863QO-G_GE0eqpvg&oe=66D9ABB9&_nc_sid=8f1549",
        "https://instagram.fdvo1-1.fna.fbcdn.net/v/t51.29350-15/413214923_348550491139881_7101861533043798366_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xNDQweDE4MDAuc2RyLmYyOTM1MC5kZWZhdWx0X2ltYWdlIn0&_nc_ht=instagram.fdvo1-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=BD4UgCO20iwQ7kNvgEl-I6j&edm=AEhyXUkBAAAA&ccb=7-5&ig_cache_key=MzI2NzM5ODA4NTQwMzkwOTEyMg%3D%3D.2-ccb7-5&oh=00_AYDWRhFiLFoCnlOXTD7XiOv8AR97CvWi1oW7GGsUQta1AQ&oe=66D9C6D3&_nc_sid=8f1549",
        "https://instagram.fdvo1-2.fna.fbcdn.net/v/t51.2885-15/56781254_270405077199654_7600902999071647230_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDgweDEzNTAuc2RyLmYyODg1LmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.fdvo1-2.fna.fbcdn.net&_nc_cat=106&_nc_ohc=tKa64tN5Ai0Q7kNvgF-A4Oz&edm=AEhyXUkBAAAA&ccb=7-5&ig_cache_key=MjAyNzM2MTk1ODI0MDgyMTk5NA%3D%3D.2-ccb7-5&oh=00_AYB-lAQU8aLxz_8d-cBGblxVPVdDZrgLJBB9YFEfcVciew&oe=66D9C134&_nc_sid=8f1549",
        "https://instagram.fdvo1-2.fna.fbcdn.net/v/t51.2885-15/56664992_2571530906406960_4776933831089548655_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDgweDEzNTAuc2RyLmYyODg1LmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.fdvo1-2.fna.fbcdn.net&_nc_cat=100&_nc_ohc=krK4v6nW4R0Q7kNvgH_-EHI&_nc_gid=ba002c1e32b74bacbc4b60503ef438e9&edm=AEhyXUkBAAAA&ccb=7-5&ig_cache_key=MjAyNjE2MzM0MTYxMDA0MzQyOA%3D%3D.2-ccb7-5&oh=00_AYDNUhuH05BVUc-4cp2S-LG5H1mSvW_1B-kwW1Dme96wJw&oe=66D9B4AD&_nc_sid=8f1549",
        "https://instagram.fdvo1-2.fna.fbcdn.net/v/t51.2885-15/56468350_328802804500159_2656959904683546271_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDgweDEzNTAuc2RyLmYyODg1LmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.fdvo1-2.fna.fbcdn.net&_nc_cat=107&_nc_ohc=DUAdOcmlJdAQ7kNvgHbs-mK&_nc_gid=ba002c1e32b74bacbc4b60503ef438e9&edm=AEhyXUkBAAAA&ccb=7-5&ig_cache_key=MjAyNTI3MTg2MzgyMDA3NjMxOA%3D%3D.2-ccb7-5&oh=00_AYBlD7HvmC-rmsj4xKbUv1UwLk6Sv-vSufjV9lOdX1r0xw&oe=66D9CADE&_nc_sid=8f1549",
        "https://instagram.fdvo1-1.fna.fbcdn.net/v/t51.2885-15/56578221_2184833571635860_5633228088602527117_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDgweDEzNTAuc2RyLmYyODg1LmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.fdvo1-1.fna.fbcdn.net&_nc_cat=104&_nc_ohc=CHz60DLlVAUQ7kNvgE-5VIV&edm=AEhyXUkBAAAA&ccb=7-5&ig_cache_key=MjAyNDQxMTI3MzA3NzYyMTAwOA%3D%3D.2-ccb7-5&oh=00_AYBEDFw7B-vdOLp1X5lhzoP8eZsSpfdtlsHuk2ExoI-6hA&oe=66D9C7BC&_nc_sid=8f1549",
        "https://instagram.fdvo1-2.fna.fbcdn.net/v/t51.2885-15/56603336_2264019470487715_3348316395030213157_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDgweDEzNTAuc2RyLmYyODg1LmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.fdvo1-2.fna.fbcdn.net&_nc_cat=107&_nc_ohc=qLBJ9gxnFCAQ7kNvgHykS84&edm=AFg4Q8wBAAAA&ccb=7-5&ig_cache_key=MjAyMzAzNDcxMDQ0MDQ1OTc3OQ%3D%3D.2-ccb7-5&oh=00_AYBzU1S5hnllC1JQm1xavK6tuF0RJNeGuQgwGEOHtXtrog&oe=66D9E1A6&_nc_sid=0b30b7",
        "https://instagram.fdvo1-2.fna.fbcdn.net/v/t51.2885-15/56852987_126184301882970_8438201883267262589_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDAweDEyNTAuc2RyLmYyODg1LmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.fdvo1-2.fna.fbcdn.net&_nc_cat=106&_nc_ohc=dZfR9aPptWwQ7kNvgGrM2Qh&edm=AFg4Q8wBAAAA&ccb=7-5&ig_cache_key=MjAyMTcyODQ4OTI5Mjc5NTcxMQ%3D%3D.2-ccb7-5&oh=00_AYCJxuzUrlbKp4jdMYT8A87Q9ZVGWr7rjWwr8tcrxGx_lg&oe=66D9CA57&_nc_sid=0b30b7",
        "https://instagram.fdvo1-1.fna.fbcdn.net/v/t51.2885-15/55827170_859683894424024_8784838179744734859_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDAweDEyNTAuc2RyLmYyODg1LmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.fdvo1-1.fna.fbcdn.net&_nc_cat=104&_nc_ohc=cg8EmtbDt3kQ7kNvgHRpTQ7&_nc_gid=0c8302c18c8e4d01982a9621016acff1&edm=AFg4Q8wBAAAA&ccb=7-5&ig_cache_key=MjAyMDg4NTU3OTYzMDU2MDM4Nw%3D%3D.2-ccb7-5&oh=00_AYBL4b_5amrH5BT262x6b1JVgk-8Rw3b-lcApjD99swL8w&oe=66D9C03F&_nc_sid=0b30b7",
        "https://instagram.fdvo1-1.fna.fbcdn.net/v/t51.2885-15/56483281_1363739250434285_5660749789801789951_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDgweDEzNTAuc2RyLmYyODg1LmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.fdvo1-1.fna.fbcdn.net&_nc_cat=105&_nc_ohc=huFxEs8rin0Q7kNvgG_FbDk&edm=AFg4Q8wBAAAA&ccb=7-5&ig_cache_key=MjAyMDI4MDk4MjI4NTE5NjI5OA%3D%3D.2-ccb7-5&oh=00_AYAm4P6KH5-36v2Kv48eaTnuFYlXzQ-oXAMRgLxO75QF2A&oe=66D9B4F9&_nc_sid=0b30b7"
    ]

# Create the directory if it doesn't exist
output_dir = "images/gallery"
os.makedirs(output_dir, exist_ok=True)

def download_image(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Extract filename from URL
        filename = os.path.basename(urlparse(url).path)
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filename += '.jpg'
        
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        # Validate file size
        file_size = os.path.getsize(filepath)
        if file_size > 0:
            print(f"Downloaded: {filename} ({file_size} bytes)")
            return True, filepath
        else:
            print(f"Error: {filename} is empty")
            os.remove(filepath)
            return False, filepath
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
        return False, None

# Use ThreadPoolExecutor for concurrent downloads
successful_downloads = 0
failed_downloads = 0

with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(download_image, gallery_images))

for success, filepath in results:
    if success:
        successful_downloads += 1
    else:
        failed_downloads += 1

print(f"\nDownload summary:")
print(f"Successful downloads: {successful_downloads}")
print(f"Failed downloads: {failed_downloads}")

# Validate the output directory
if os.path.exists(output_dir):
    files_in_dir = os.listdir(output_dir)
    print(f"\nFiles in {output_dir}: {len(files_in_dir)}")
    
    if len(files_in_dir) > 0:
        print("Sample files:")
        for file in files_in_dir[:5]:  # Show up to 5 files
            file_path = os.path.join(output_dir, file)
            file_size = os.path.getsize(file_path)
            print(f"- {file} ({file_size} bytes)")
    else:
        print("No files found in the output directory.")
else:
    print(f"Error: {output_dir} does not exist.")

# Calculate total size of downloaded files
total_size = sum(os.path.getsize(os.path.join(output_dir, f)) for f in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, f)))
print(f"\nTotal size of downloaded files: {total_size} bytes ({total_size / (1024*1024):.2f} MB)")

print("\nAll downloads completed.")