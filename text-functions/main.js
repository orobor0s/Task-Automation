document.querySelector('button').addEventListener('click', (e) => {
    console.log(document.querySelector('#text-functions').value)
    selectFunction(document.querySelector('#text-functions').value)
})

// calls function based on dropdown value
function selectFunction(textFunction) {
    if (textFunction == 'title-to-normal') {
        titleToNormal()
    }
}

// converts title case to normal case and copies output to clipboard
function titleToNormal() {
    let text = document.querySelector('input').value.split(' ')
    for (let i = 1; i < text.length; i++) {
        text[i] = text[i].split('')
        text[i][0] = text[i][0].toLowerCase()
        text[i] = text[i].join('')
    }
    text = text.join(' ')
    copyToClipboardAsync(text)
    document.querySelector('input').value = ''
}

// function that copies string to clipboard
const copyToClipboardAsync = str => {
  if (navigator && navigator.clipboard && navigator.clipboard.writeText)
    return navigator.clipboard.writeText(str);
  return Promise.reject('The Clipboard API is not available.');
}