const imageBox = document.getElementById('img-box')
const image = document.getElementById('id_image')


const url = ""

image.addEventListener('change', ()=>{
    const image_data = image.files[0]
    const url = URL.createObjectURL(image_data)
    console.log(url)
    imageBox.innerHTML = `<img src="${url}" width="100px">`
})
