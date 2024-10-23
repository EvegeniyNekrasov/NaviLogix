import { ReactNode } from "@tanstack/react-router";

interface CardProp {
    children: ReactNode;
}

const Card: React.FC<CardProp> = ({ children }) => {
    return (
        <div
            className={
                "w-full h-full p-4 rounded-xl bg-slate-100 dark:bg-slate-800 flex flex-col gap"
            }>
            {children}
        </div>
    );
};

export default Card;
