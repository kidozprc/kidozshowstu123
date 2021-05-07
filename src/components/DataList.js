import React, { useState, useEffect } from 'react'
import firebase from '../utils/firebase'
import Data from './Data'

function DataList(){

    const [dataList, setDataList] = useState();

    useEffect(() =>{
        const dataRef = firebase.database().ref('ForWeb');
        // listen every time data change in data ref
        dataRef.on('value', (snapshot) => {
            const datas = snapshot.val();
            const dataList = [];
            for (let id in datas) {
                dataList.push({ id, ...datas[id]});
            }
            setDataList(dataList);
        })
    }, [])

    return(
        <div className="getrotate">
            {dataList ? dataList.map((data, index) => <Data data = {data} key={index} />) : ""}
        </div>
    )
}

export default DataList;