import sqlite3

# Creating and connecting database
conn = sqlite3.connect("youtube_with_DB.db")
cursor = conn.cursor() # cursor is used for executing quries

# Creating a table 
cursor.execute('''  
    CREATE TABLE IF NOT EXISTS videos(
            id  INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
           )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id))
    conn.commit()

def main():
    while True:
        print("\n Youtube Manager | Choose an option!")
        print("1. List all youtube videos.")
        print("2. Add a youtube video.")
        print("3. Update a youtube video details.")
        print("4. Delete a youtube video.")
        print("5. Exit the app.")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()

        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)

        elif choice == "3":
            video_id = input("Enter video Id to update video: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)

        elif choice == "4":
            video_id = input("Enter video Id to delete video: ")
            delete_video(video_id)

        elif choice == "5":
            break

        else:
            print("Invalid choice!")

    conn.close()


if __name__ == "__main__":
    main()