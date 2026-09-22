import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const signUpPromise = signUpUser(firstName, lastName)
    .then((value) => ({ status: 'fulfilled', value }))
    .catch((err) => ({ status: 'rejected', value: err.toString() }));

  const uploadPhotoPromise = uploadPhoto(fileName)
    .then((value) => ({ status: 'fulfilled', value }))
    .catch((err) => ({ status: 'rejected', value: err.toString() }));

  return Promise.all([signUpPromise, uploadPhotoPromise]);
}