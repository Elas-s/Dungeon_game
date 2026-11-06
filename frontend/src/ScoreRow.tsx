type ScoreRowProps = {
    rank: number
    name: string
    gold: number
}
const MEDALS: Record<number, string> = {1: "🥇", 2: "🥈", 3: "🥉"}
function ScoreRow({ rank, name, gold}:ScoreRowProps){
    return(
        <div className={"score-row"}>
            <span> {MEDALS[rank] ?? `- ${rank}`} </span>
            <span> {name} </span>
            <span> 💰 {gold} </span>
        </div>
    )
}


export default ScoreRow