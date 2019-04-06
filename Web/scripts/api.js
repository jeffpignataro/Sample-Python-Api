async function PostRequest(url, method = "POST", data = {}) {
    const promise = await fetch(url, {
        method: method, // POST, PUT, DELETE, etc.
        mode: "no-cors", // no-cors, cors, *same-origin
        cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
        credentials: "same-origin", // include, *same-origin, omit
        headers: {
            "Content-Type": "application/json",
            // "Content-Type": "application/x-www-form-urlencoded",
        },
        redirect: "follow", // manual, *follow, error
        referrer: "no-referrer", // no-referrer, *client
        body: JSON.stringify(data), // body data type must match "Content-Type" header

    });
    const response = await promise.json();
    return response;
}

async function GetRequest(url, method = "GET") {
    const promise = await fetch(url);
    const data = await promise.json();
    return data;
}
