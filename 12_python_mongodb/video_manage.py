# import pymongo
# Add Mongo Db URI
# client = pymongo.MongoClient("MONGODB_URI")
# print(client)
from pymongo import MongoClient # type: ignore
from bson import ObjectId # type: ignore

client = MongoClient("MONGODB_URI")
print(client)

db = client["ytmanager"]

video_collection = db["videos"]

print(video_collection)


def list_videos():
    # Returns an interable
    for video in video_collection.find():
        print(f"ID :{video['_id']} Name: {video['name']} ,Time: {video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name":name,"time":time})

def update_video(video_id,name,time):
    # First parameter what to update Second parameter updated value
    video_collection.update_one({'_id':ObjectId(video_id)},{'$set':{"name":name,"time":time}})

def delete_video(video_id):
    video_collection.delete_one({"_id":ObjectId(video_id)})

def main():
    while True:
        print("Video Manager with DB")
        print("1. List all Videos")
        print("2. Add a Video")
        print("3. Update a video deatils")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter Video Name: ")
            time = input("Enter Video Time: ")
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter Video ID to update:  ")
            name = input("Enter Video Name: ")
            time = input("Enter Video Time: ")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id = input("Enter Video ID to delete:  ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()