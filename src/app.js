import Amplify, { API } from 'aws-amplify';
import awsconfig from './aws-exports';

Amplify.configure(awsconfig);

async function getData() { 
    let apiName = 'randomheroes';
    let path = '/randomheroes';
    let myInit = { // OPTIONAL
        headers: {} // OPTIONAL
    }
    return await API.get(apiName, path, myInit);
}

const MutationButton = document.getElementById('MutationEventButton');
const MutationResult_heroe1 = document.getElementById('MutationResult_heroe1');
const MutationResult_heroe2 = document.getElementById('MutationResult_heroe2');
const MutationResult_heroe3 = document.getElementById('MutationResult_heroe3');

MutationButton.addEventListener('click', (evt) => {
    // getting the first random hero
    getData().then( (response) => {
        MutationResult_heroe1.innerHTML = `<p> ${response['heroe_1'].Name} - ${response['heroe_1'].Type}</p><img src="${response['heroe_1'].Picture}" alt="heroe1" width="100" height="100">`
        MutationResult_heroe2.innerHTML = `<p> ${response['heroe_2'].Name} - ${response['heroe_2'].Type}</p><img src="${response['heroe_2'].Picture}" alt="heroe2" width="100" height="100">`
        MutationResult_heroe3.innerHTML = `<p> ${response['heroe_3'].Name} - ${response['heroe_3'].Type}</p><img src="${response['heroe_3'].Picture}" alt="heroe3" width="100" height="100">`
      });
});