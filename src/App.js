import './App2.css';
import DataList from './components/DataList'
// import AddData from './components/AddData'
import ShowHeader from './ShowHeader'
import ShowTop from './ShowTop'

export default function App() {
  return (
    <div className="App">
      <ShowHeader />
      <ShowTop />
      <DataList />
      {/* <AddData /> */}
    </div>
  );
}

