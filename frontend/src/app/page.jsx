import React from "react";

function HomePage() {
    return (
        <div className="homePage">
            <h2 className="title">Hosted Inference API</h2>

            <div className="content">
                <div className="titleQA">
                    <span>Question Answering</span>
                </div>
            </div>
            <form className="space-y-2">
                <div className="qA">
                    <input className="qAInput" type="text" placeholder="Your sentence here..." required />
                    <button className="btnCompute" type="submit">
                        Compute
                    </button>
                </div>
                <label style={{display:"block"}}> 
                    <span className="titleContext">
                        Context
                    </span> 
                    <span className="inputContent focus:shadow-inner dark:bg-gray-925 svelte-1wfa7x9" role="textbox" contenteditable="" spellcheck="false" dir="auto">
                        Phạm Văn Đồng (1 tháng 3 năm 1906 – 29 tháng 4 năm 2000) là Thủ tướng đầu tiên của nước Cộng hòa Xã hội chủ nghĩa Việt Nam từ năm 1976 (từ năm 1981 gọi là Chủ tịch Hội đồng Bộ trưởng) cho đến khi nghỉ hưu năm 1987. Trước đó ông từng giữ chức vụ Thủ tướng Chính phủ Việt Nam Dân chủ Cộng hòa từ năm 1955 đến năm 1976. Ông là vị Thủ tướng Việt Nam tại vị lâu nhất (1955–1987). Ông là học trò, cộng sự của Chủ tịch Hồ Chí Minh. Ông có tên gọi thân mật là Tô, đây từng là bí danh của ông. Ông còn có tên gọi là Lâm Bá Kiệt khi làm Phó chủ nhiệm cơ quan Biện sự xứ tại Quế Lâm (Chủ nhiệm là Hồ Học Lãm).
                    </span>
                </label>
            </form>
            <div className="answer">
                <span>Lâm Bá Kiệt</span> 
                <span className="score">0.805</span>
            </div>
        </div>
    )
}

export default HomePage;

