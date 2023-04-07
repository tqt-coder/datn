import NewChat from "./NewChat"
import '../App.css';

function SideBar() {
  return (
    <div className="side">
      <div className="bar">
        <div>

          {/* NewChat */}
          <NewChat />
          <div>
            {/* ModelSelection */}
          </div>

          {/* Map through the ChatRows */}

        </div>
      </div>
    </div>
  )
}

export default SideBar