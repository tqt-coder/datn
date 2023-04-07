import React from "react";
import { PaperAirplaneIcon } from "@heroicons/react/24/solid"
import '../App.css';

function ChatInput() {

    return (
        <div className="chat">
            <form className="frame">
                <input 
                    className="bg-transparent focus:outline-none flex-1
                    disabled:cursor-not-allowed disabled:text-gray-300"
                    type="text"
                    placeholder="Type your message here..." 
                />

                <button
                    type="submit"
                    className="submit"
                >
                    <PaperAirplaneIcon className="iconChat" />
                </button>
            </form>

            <div></div>
        </div>
    )
}

export default ChatInput;