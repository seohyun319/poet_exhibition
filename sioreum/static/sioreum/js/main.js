const request = new XMLHttpRequest();
    
    const btn = document.querySelector(".uploadBtn");
    const textarea = document.querySelector(".visitContent");
    const namearea = document.querySelector(".author");
    const numberarea = document.querySelector(".number");
    
    btn.addEventListener('click', () => {
        onClick();
    })

    textarea.addEventListener('input', () => {
        validText();
    })
    
    namearea.addEventListener('input', () => {
        validName();
    })
    
    const validText = () => {
        if (namearea.value && textarea.value) {
            btn.classList.add('active');
            return true;           
        } if (!textarea.value) {
            alert("내용을 작성해주세요.")
            btn.classList.remove('active');
            return false;
        } 
    }
    
    const validName = () => {
        if (namearea.value && textarea.value) {
            btn.classList.add('active');
            return true;        
        } if (!namearea.value) {
            btn.classList.remove('active');
            alert("이름을 작성해주세요.")
            return false;
        }             
    }

    const onClick = () => {
        const content = textarea.value;
        const name = namearea.value;
        const number = numberarea.value;
        if(!validText() && !validName()) return
        const url = "/visitor/write/";
        request.open("POST", url, true);
        request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        request.send(JSON.stringify({ content, name, number }));
        textarea.value = ""; 
        namearea.value = ""; 
        numberarea.value = "";
    };

    const handleResponse = () => {
        if (request.status <= 400) {
            const { comment, writer, time } = JSON.parse(request.response);         
            const element = document.querySelector(".visitContainer")
            const createVisit = document.createElement("div");
            const dateTime = new Date(time) 
            const newTime = dateTime.toLocaleDateString('en-US', {year: '2-digit'}) + "." +
                            dateTime.toLocaleDateString('en-US', {month: '2-digit'}) + "." +
                            dateTime.toLocaleDateString('en-US', {day: '2-digit'})           
            createVisit.innerHTML = `
                <div class="m-3 px-3 pt-3 card">
                    <div class="overflow-auto" style="height:130px;">${ comment }</div>
                        <div class="row row-cols-3 px-3 mt-2">
                        <div class="mt-2 author">${ writer }</div>
                        <img src="static/sioreum/img/flower.png" class="flower" alt="">
                        <div class="mt-2 text-right text-secondary" style="height:25px;">${ newTime } </div>
                    </div>
                </div>
                `;
            element.insertBefore(createVisit, element.children[1]);
            element.children[8].hidden=true;
        }
    };
   
    request.onreadystatechange = () => {
        if (request.readyState === XMLHttpRequest.DONE) {
            handleResponse();
        }
    };

    //btn disabled, numberFormat, pagination ajax hidden false