import { useState } from "react";
import OutReachModal from "./OutReachModal";

function PropertyCard({ property }){
    const [script, setScript] = useState(null)
    const [loading, setLoading] = useState(false)
    const [showModal, setShowModal] = useState(false)

    const handleGenerate = async () => {
        setLoading(true);

        const response = await fetch("/api/generate-outreach",{
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify(property)
        })

        const data = await response.json()

        setScript(data.script)
        setLoading(false)
        setShowModal(true)
    }

    const formatValue = (value) => {
        return '$' + value.toLocaleString()
    }

    const typeColor = {
        'Office Building': 'bg-blue-100 text-blue-700',
        'Retail Strip': 'bg-purple-100 text-purple-700',
        'Mixed Use': 'bg-orange-100 text-orange-700',
        'Warehouse': 'bg-yellow-100 text-yellow-700',
    }

    return (
        <>
            <div className="bg-white rounded-2xl shadow-md hover:shadow-lg transition p-5 flex flex-col gap-4">
                <div className="flex justify-between items-start">
                    <h3>{property.owner_name}</h3>
                    <p>{property.property_address}, {property.city}</p>
                </div>
                <span>
                    {property.property_type}
                </span>
            </div>

            <div>
                <div>
                    <p>Years Owned</p>
                    <p>{property.years_owned}</p>
                </div>

                <div>
                    <p>Sq Ft</p>
                    <p>{property.sq_ft.toLocaleString()}</p>
                </div>

                <div>
                    <p>Est. Value</p>
                    <p>{formatValue(property.assessed_value)}</p>
                </div>

                <button>
                    {loading ? 'Generating...' : 'Generate Outreach Script'}
                </button>

            </div>

            {showModal && (
                <OutReachModal
                    script = {script}
                    owner = {property.owner_name}
                    onClose={() => setShowModal(false)}
                />
            )}

            

        </>
    )

}
export default PropertyCard;