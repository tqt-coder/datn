import './App.css';
import HomePage from './app/page'
import SideBar from './components/SideBar';

function App() {
  return (
    <div className="App">
        <div className="sideBar">
            <SideBar />
      </div>
      <div className="ClientProvider">
        <HomePage/>
      </div>
    </div>
  );
}

export default App;
