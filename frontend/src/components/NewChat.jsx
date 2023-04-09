import { PlusIcon } from "@heroicons/react/24/solid";
import '../App.css';

function NewChat() {
    return (
        <div className="newChat chatRow">
            <PlusIcon className="iconChat" />
            <p>New Example</p>
        </div>
    );
}

export default NewChat;