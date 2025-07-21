import sqlite3
conn = sqlite3.connect('youtube_videos.db')
cur = conn.cursor()

cur.execute(''' 
CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )
 ''')

def list_videos():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)

def add_video(name,time):
    cur.execute("INSERT INTO videos (name,time) VALUES (?,?)", (name,time))
    conn.commit()

def update_video(video_id,new_name,new_time):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name,new_time,video_id))
    conn.commit()

def delete_video(video_id):
    cur.execute("DELETE FROM videos where id=?",(video_id,))
    conn.commit()


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
            video_id = input("Enter Video ID to update:  ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")
    conn.close()

if __name__ == "__main__":
    main()