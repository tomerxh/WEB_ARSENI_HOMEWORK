console.log("im inside fetch example");

function get_users(){
    console.log("click");
    //אנחנו רוצים למשוך נתונים ממשאב אחר, הנתונים מתקבלים כאן בצורה ג'ייסון, נרצה להפוך את הג'ייסון לאובייקט כך שיתאים לגאווה סקריפט
    // פה הפונקציה שולחת בקשה ומקבלת רספונס
    fetch('https://reqres.in/api/users?page=2').then(
        // input -> output
        response => response.json() //להמיר מג'ייסון לאובייקט
    ).then(
        response_obj => put_users_inside_html(response_obj.data) // data is a specific key in the dict
    ).catch(
        err => console.log(err)
    )
}

// רק החלק הספציפי של היוזרים מתעדכן כאשר לוחצים על הכפתור
function put_users_inside_html(response_obj_data){
    // console.log(response_obj_data)
    const curr_main = document.querySelector("main"); //רוצים לתפוס את התגית main
    for(let user of response_obj_data){
        const section = document.createElement('section');
        // the $ is for string with variables
        // mailto is a protocol for emails
        section.innerHTML = `
        <img src="${user.avatar}" alt="Profile Picture"/> 
        <div>
            <span> ${user.first_name} ${user.last_name}</span>
            <br>
            <a href="mailto:${user.email}">Send Email</a>   
        </div>
        `;
        curr_main.appendChild(section);
    }
}