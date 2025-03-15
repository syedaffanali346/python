from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017") # Connect to the database
db = client["youtube_manager_with_python"]         # Create a databese
collection = db["yt_manager"]                       # Create a collection / table

print(collection)

def list_videos():
    for video in collection.find():
        print(f"ID: {video["_id"]}, Name: {video["name"]} and Time: {video["time"]}")

def add_video(name, time):
    collection.insert_one({"name": name, "time": time})

def update_video(video_id, name, time):
    print(ObjectId(video_id))
    collection.update_one(
        {"_id": ObjectId(video_id)},
        {"$set": {"name": name, "time": time}}
    )

def delete_video(video_id):
    collection.delete_one({"_id": ObjectId(video_id)})

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

if __name__ == "__main__":
    main()