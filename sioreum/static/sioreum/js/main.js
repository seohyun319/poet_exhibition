const request = new XMLHttpRequest();

const onClick = () => {
    const textarea = document.querySelector(`textarea`);
    const content = textarea.value;
    const url = "/visitor/write/";
    request.open("POST", url, true);
    request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    request.send(JSON.stringify({ content }));
    textarea.value = "";
};