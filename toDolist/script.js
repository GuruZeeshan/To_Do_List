const containerEle=document.getElementById('container');
const mainEle=document.getElementById('main');

const dummyEle=document.getElementById('dummy');
const inputText=document.getElementById('input');

const addBtn=()=>{

    const createDiv=document.createElement("div");
    const createList=document.createElement("ul");
    createDiv.appendChild(createList);
    const createButton= document.createElement("button");
    createDiv.appendChild(createButton);

    
    // createDiv.setAttribute("id","1st");
    // const createList=document.createElement("ul");
    createList.innerHTML=`<i class="fa-sharp fa-solid fa-circle-info"></i> 
    ${inputText.value}`;
  createButton.innerHTML=
    `<i class="fa-solid fa-trash-can"></i>`;
    dummyEle.appendChild(createDiv);
    createButton.addEventListener('click',function(){
      createDiv.remove();
    })

    
  

       
}
