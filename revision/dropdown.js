const brandSelect = document.getElementById('brand');
const modelSelect = document.getElementById('model');

const brands = {
  maruti: ['800', 'swift', 'desire'],
  tata: ['tiago','tigor', 'nexon'],
  hundai: ['i10', 'i20', 'creta']
}

function modelSelectValue() {
  const brand = brandSelect.value
  const options = function() {
    let text = ``
    brands[brand].forEach(brandValue => {
      text = text + `<option value=${brandValue}>${brandValue.toUpperCase()}</option>`
    });
    return text
  }
  modelSelect.innerHTML = options()
}

modelSelectValue()

brandSelect.addEventListener('change', modelSelectValue)