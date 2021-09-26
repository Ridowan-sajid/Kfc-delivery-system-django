let helptext=document.querySelectorAll('.helptext')

Array.from(helptext).forEach((h)=>{
 h.remove();
})
// Array.from(document.getElementsByTagName('label')).forEach((h)=>{
//  h.remove();
// })

Array.from(document.getElementsByTagName('br')).forEach((h)=>{
 h.remove();
})






