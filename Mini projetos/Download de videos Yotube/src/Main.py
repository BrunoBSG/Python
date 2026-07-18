from downloader import Downloader



def main():

    print("=" * 50)
    print("AutoShorts")
    print("=" * 50)

    url = input("Cole a URL do vídeo: ")

    downloader = Downloader()

    video_path = downloader.download(url)



    print("\nVídeo:")
    print(video_path)




if __name__ == "__main__":
    main()