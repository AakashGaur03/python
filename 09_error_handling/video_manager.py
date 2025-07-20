import json
def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file) # gets file data and converts it in json
    except (FileNotFoundError, json.JSONDecodeError):
        return []
        
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file) # writes in file first parameter what to write second parameter where to write
    
def list_all_videos(videos):
    # enumerate(videos, start=1) # covnerts in list with numbers like [(0,value),(1,value)] when do start =1 then start index from 1
    print('\n')
    print('*' * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} , duration: {video['time']} ")
    print('*' * 70)
    print('\n')


def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter Video number to update: "))
    if 1<= index <= len(videos):
        name = input("Enter new video Name")
        time = input("Enter new video Time")
        videos[index-1] = {'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid Index Selected")


def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter Video number to delete: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid Index Selected")

def main():
    videos = load_data()
    while True:
        print("Video Manager")
        print("1. List all Videos")
        print("2. Add a Video")
        print("3. Update a video deatils")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid")

if __name__ == "__main__":
    main()