const startCity = document.getElementById('start_input')
const endCity = document.getElementById('end_input')
const res_box = document.getElementById('res_box')


async function send() {
    try {

        const res = await fetch(`/api/weather?start=${startCity.value}&end=${endCity.value}`, {
                method: 'GET', 
                mode: 'cors', 
                cache: 'no-cache',
                headers: {'Content-Type': 'application/json'},
                redirect: 'follow',
                referrerPolicy: 'no-referrer'
            });
        const result = (await res.json())
        if (result.start.precipitation == 1) {
            result.start.precipitation = 'есть'
        }
        else {
            result.start.precipitation = 'нету'
        }
        if (result.end.precipitation == true) {
            result.end.precipitation = 'есть'
        }
        else {
            result.end.precipitation = 'нету'
        }
        if (result.start.is_bad == true) {
            result.start.precipitation = 'погода плохая'
        }
        else {
            result.start.precipitation = 'погода хорошая'
        }
        if (result.end.precipitation == true) {
            result.end.precipitation = 'погода хорошая'
        }
        else {
            result.end.precipitation = 'погода плохая'
        }
        res_box.innerHTML = ""
        html1 = `<div><div><h1> ${startCity.value.toUpperCase()} </h1></div> <div>Температура: ${result.start.temp}</div> <div>Скорость ветра: ${result.start.wind}</div> <div>Вердикт: ${result.start.precipitation}</div></div>`
        res_box.insertAdjacentHTML('beforeend', html1)
        html2 = `<div><div><h1> ${endCity.value.toUpperCase()} </h1></div> <div>Температура: ${result.end.temp}</div> <div>Скорость ветра: ${result.end.wind}</div> <div>Вердикт: ${result.end.precipitation}</div></div>`
        res_box.insertAdjacentHTML('beforeend', html2)
    } catch {
        alert('Error!')
    }
    
}
