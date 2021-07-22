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

// btn.addEventListener('click', async () => {
//     const textarea = document.querySelector(".visitContent");
//     const content = textarea.value;
//     if (!content) {
//         return;
//     }
//     axios.defaults.xsrfCookieName = "csrftoken";
//     axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
//     const url = '/visitor/write/';
//     const { data } = await axios.post(url, {
//         content,
//     });
//     modify(data);
//     textarea.value = "";
// });



// const onClick = () => {
//     const textarea = document.querySelector(`textarea`);
//     const content = textarea.value;
//     const url = "/visitor/write/";
//     request.open("POST", url, true);
//     request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
//     request.send(JSON.stringify({ content }));
//     textarea.value = "";
// };