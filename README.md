# HARINI.20
A To-Do List App helps users manage tasks by allowing them to create, read, update, and delete tasks (commonly called CRUD operations). Here's a high-level overview of how it works:


---

🛠️ Working of a To-Do List App

1. User Interface (UI)

Users interact with the app through a visual interface:

Input Field – to type new tasks.

Add Button – to add a task to the list.

Task List – shows all tasks, often with checkboxes to mark them complete.

Edit/Delete Buttons – for managing tasks.



---

2. Core Functionalities

✅ Add Task

User types in a task and clicks "Add".

The app stores this task in a data structure (e.g., an array or database).


📋 Display Task

The app retrieves tasks from storage.

It displays them in the list with options to mark as done, edit, or delete.


🖊️ Edit Task

User clicks “Edit”.

The task text becomes editable.

On save, the task is updated in the storage.


🗑️ Delete Task

User clicks “Delete”.

The task is removed from the storage and the UI.


✅ Mark as Complete

User ticks a checkbox or taps a "done" button.

The task is marked completed (e.g., with a strikethrough or a different color).



---

3. Storage Options

a. Local Storage (Web/Offline apps)

Uses browser’s localStorage or IndexedDB.

Tasks persist even after refreshing the page.


b. Database (Web/Cloud/Mobile apps)

Firebase, MongoDB, MySQL, etc.

Allows syncing across multiple devices.



---

4. Backend (Optional)

In a full-stack app:

A server handles requests (using Node.js, Django, etc.).

APIs (REST or GraphQL) handle CRUD operations with a database.



---

5. Technologies Used

Frontend: HTML, CSS, JavaScript, React, Vue,


