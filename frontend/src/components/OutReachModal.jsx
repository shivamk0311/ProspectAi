function OutReachModal({script, owner, onClose}){

    const handleCopy = () => {
        navigator.clipboard.writeText(script);
        alert('Script copied to clipboard');
    }

    return (
        <div
            className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4"
            onClick={onClose}
        >
            <div
                className="bg-white rounded-2xl shadow-2xl max-w-lg w-full p-6"
                onClick={(e) => e.stopPropagation()}
            >
                <div>
                    <h2
                        className="text-lg font-bold text-gray-600"
                    >
                        Outreach Script - {owner}
                    </h2>
                    <button
                        className="text-gray-400 hover:text-gray-600 text-2xl leading-none"
                        onClick={onClose}
                    >
                        &times;
                    </button>
                </div>

                <div
                    className="bg-gray-50 text-sm p-4 rounded-xl text-gray-700 leading-relaxed whitespace-pre-wrap"
                >
                    {script}
                </div>

                <div className="flex gap-3 mt-5">
                    <button
                        onClick={handleCopy}
                        className="flex-1 bg-green-600 hover:bg-green-700 text-white font-semibold py-2 rounded-xl transition"
                    >
                        Copy Script
                    </button>
                    <button
                        onClick={onClose}
                        className="flex-1 bg-gray-100 hover:bg-gray-200 text-gray-700 font-semibold py-2 rounded-xl transition"
                    >
                        Close
                    </button>
                </div>


            </div>

        </div>
    )

}

export default OutReachModal;