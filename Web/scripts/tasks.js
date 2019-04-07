window.onload = function() {
    document.getElementById("getTasks-button").onclick = function() {
        GetTasks();
    };
    document.getElementById("getTask-button").onclick = function() {
        taskList = document.getElementById("task-list");
        selectedItem = taskList.value;
        if (selectedItem === "0") {
            error = "Error: No task selected.";
            console.log(error);
            return error;
        }
        GetTask(selectedItem);
    };
};

async function GetTasks() {
    getTasks = await GetRequest("http://127.0.0.1:5000/todo/api/v1.0/tasks");
    returnJson = JSON.stringify(getTasks);
    console.log(returnJson);
    document.getElementById("tasks-result").innerHTML = returnJson;
}

async function GetTask(id) {
    getTask = await GetRequest(`http://127.0.0.1:5000/todo/api/v1.0/tasks/${id}`);
    returnJson = JSON.stringify(getTask);
    console.log(returnJson);
    document.getElementById("tasks-result").innerHTML = returnJson;
}
