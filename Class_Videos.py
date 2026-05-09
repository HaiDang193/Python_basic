class Video:
    def __init__(self,title,link):
        self.title = title
        self.link = link

def read_video():
    title = input("Enter the title: ")
    link = input("Enter the link: ")
    video = Video(title,link)
    return video

def read_videos():
    videos = []
    total_video = int(input("Enter how many videos: "))
    for i in range(total_video):
        print("Enter video", i+1)
        vid = read_video()
        videos.append(vid)
    return videos

def write_video_txt(video,file):
    file.write("title:"+video.title + "\n")
    file.write("link:"+video.link + "\n")

def write_to_txt(videos):
    total = len(videos)
    with open("data.txt", "w") as file:
        file.write(f"There are {total} videos:\n")
        for i in range(total):
            file.write(f"Video {i+1}\n")
            write_video_txt(videos[i],file)

def print_video(video):
    print("Title:"+video.title)
    print("Link:"+video.link)

def print_videos(videos):
    for i in range(len(videos)):
        print(f"Video {i+1}")
        print_video(videos[i])

def main():
    videos = read_videos()
    write_to_txt(videos)
    print("---")
    print_videos(videos)

main()