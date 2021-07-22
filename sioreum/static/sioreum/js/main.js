const request = new XMLHttpRequest();

const btn = document.querySelector(".uploadBtn");
btn.addEventListener('click', () => {
    const textarea = document.querySelector(".visitContent");
    const content = textarea.value;
    const url = '/visitor/write/';
    request.open("POST", url, true);
    request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    request.send(JSON.stringify({ content:content }));
    // textarea.value = "";
});

// const onClick = () => {
//     const textarea = document.querySelector(`textarea`);
//     const content = textarea.value;
//     const url = "/visitor/write/";
//     request.open("POST", url, true);
//     request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
//     request.send(JSON.stringify({ content }));
//     textarea.value = "";
// };