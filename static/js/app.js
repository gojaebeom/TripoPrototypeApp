const signModalBackground = document.querySelector('.sign-modal-background');
const signModalWrap       = document.querySelector('.sign-modal-wrap');
const signCloseButton         = document.querySelector('.sign-close-button');
const signOpenButton         = document.querySelector('.sign-open-button');

if(signOpenButton){
    signOpenButton.onclick = () => {
        console.log('sign open button click!');
        signModalBackground.style.display = 'flex';
    }
}

if(signCloseButton){
    signCloseButton.onclick = () => {
        console.log('sign close button click!');
        signModalBackground.style.display = 'none';
    }
}