window.onload = async function() {
    getRequest = await GetRequest("http://127.0.0.1:5000/");
    document.getElementById("api-result").innerHTML = getRequest.data;
};
