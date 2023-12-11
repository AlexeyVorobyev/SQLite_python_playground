const form = document.getElementById('form')
const input_region_id = document.getElementById('input_region_id')

form.addEventListener('submit', (event) => {
    event.preventDefault()
    console.log(input_region_id.value)
    fetch(`http://localhost:3001/api/regions/${input_region_id.value}`, {
        method: 'GET'
    })
    setTimeout(() => {
        window.location = `/regions/table.html`
    },2000)
})