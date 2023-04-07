import React from "react";
import { SunIcon, BoltIcon, ExclamationTriangleIcon } from '@heroicons/react/24/outline';
import '../App.css'

function HomePage() {
    return (
            <div className="homePage">
                <h1 className="title">ChatGPT</h1>

                <div className="content">
                    <div>
                        <div className="col">
                            {/* Sun Icon */}
                            <SunIcon className="icon" />
                            <h2>Examples</h2>
                        </div>

                        <div className="space-y-2">
                            <p className="infoText">Explain Something to me</p>
                            <p className="infoText">
                                What is the difference between a dog and a cat?
                            </p>
                            <p className="infoText">What is the color of the sun?</p>
                        </div>
                    </div>

                    <div>
                        <div className="col">
                            {/* Sun Icon */}
                            <BoltIcon className="icon" />
                            <h2>Capabilities</h2>
                        </div>

                        <div className="space-y-2">
                            <p className="infoText">Remembers what user said eaelier in the conversation</p>
                            <p className="infoText">
                                Allows user to provide follow-up corrections
                            </p>
                            <p className="infoText">Trained to decline inappropriate requests</p>
                        </div>
                    </div>

                    <div>
                        <div className="col">
                            {/* Sun Icon */}
                            <ExclamationTriangleIcon className="icon" />
                            <h2>Limitations</h2>
                        </div>

                        <div className="space-y-2">
                            <p className="infoText">May occasionally generate incorrect information</p>
                            <p className="infoText">
                                May occasionally produce harmful instructions or biased content
                            </p>
                            <p className="infoText">Limited knowledge of world and events after 2022</p>
                        </div>
                    </div>
                </div>
            </div>
    )
}

export default HomePage;