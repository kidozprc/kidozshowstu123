import firebase from 'firebase'

var firebaseConfig = {
  apiKey: "AIzaSyC5jORXlEZjlJQJw2WqroTYvUtYbdUtfyY",
  authDomain: "kidozprc2021.firebaseapp.com",
  databaseURL: "https://kidozprc2021-default-rtdb.firebaseio.com",
  projectId: "kidozprc2021",
  storageBucket: "kidozprc2021.appspot.com",
  messagingSenderId: "634637135157",
  appId: "1:634637135157:web:f6e173f1904d66d6d7b07c",
  measurementId: "G-CPZBC8HR2K"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();

export default firebase;