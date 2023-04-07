import HomePage from './app/page';
import ChatInput from './components/ChatInput';
import SideBar from './components/SideBar';
import './App.css'

function App() {
  return (
    <div className='app'>
      <div className="sideBar">
            <SideBar />
      </div>
      <div className="ClientProvider">
        <HomePage/>
        <ChatInput/>
      </div>
    </div>
  );
}

export default App;
