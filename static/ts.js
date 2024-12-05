function post(url, data) {
    const request_form = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }
    return fetch(url, request_form);
}

async function translate() {
    try {
        const url = "/translater";
        const en = document.getElementById("english").value
        const data = {'content': en}
        const response = await post(url, data);
        const result = await response.json();
        document.getElementById("finnish").textContent = result.translation_res;
    } catch (error) {
        console.error("Error:", error);
    }
}

compute_button = document.getElementById("compute")
compute_button.addEventListener("click", translate)

