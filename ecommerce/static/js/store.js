function tog(){
				let x = document.querySelector('.link2');
				let y = document.querySelector('.burg1');
				let b = document.querySelector('.burg2');
				let a = document.querySelector('.burg3');
				x.classList.toggle('toggle');
				y.classList.toggle('tog');
				a.classList.toggle('tog');
				b.classList.toggle('tog');
                }


var updateBtns = document.getElementsByClassName('update-cart')
for (i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId= this.dataset.product
        var action= this.dataset.action
        console.log('productId:', productId, 'action:', action )

        console.log('USER:', user)
        if (user == 'AnonymousUser'){
            alert('You need to login to use this feature')
            console.log('User is not authenticated')
        
        }
        else {
            updateUserOrder(productId,action)
        }

    })

};
function updateUserOrder(productId, action){
    console.log('User is authenticated, sending data..')

    var url = '/update_item/'
    console.log('Url:', url)
    
    fetch(url, {
        method:'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload()
    });
}