import React, { Component } from 'react'
import firebase from '../utils/firebase'
import '../App2.css'
import Sound from 'react-sound';

export default function Data({ data }) {

    return (
        <div className="stu">
            <div className="getrotate">{data.name + "  " + data.room}</div>
        </div>
    )
}
