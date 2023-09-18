function toggleModal() {
    document.querySelector('.modal').classList.toggle('is-active')
}

function deleteItem(pk) {
    document.cookie = 'pk=' + pk
    toggleModal()
}

