import React, { ReactNode, useState, useRef, useEffect } from "react";

interface TooltipProps {
    content: string;
    children: ReactNode;
    position?:
        | "top-left"
        | "top"
        | "top-right"
        | "bottom-left"
        | "bottom"
        | "bottom-right"
        | "left"
        | "right";
}

const Tooltip: React.FC<TooltipProps> = ({
    content,
    children,
    position = "top",
}) => {
    const [visible, setVisible] = useState(false);
    const [tooltipStyles, setTooltipStyles] = useState({});
    const tooltipRef = useRef<HTMLDivElement>(null);
    const wrapperRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (visible && tooltipRef.current && wrapperRef.current) {
            const tooltipRect = tooltipRef.current.getBoundingClientRect();
            const wrapperRect = wrapperRef.current.getBoundingClientRect();
            const screenWidth = window.innerWidth;
            const screenHeight = window.innerHeight;

            let styles: React.CSSProperties = {};

            switch (position) {
                case "top":
                    styles = {
                        left: "50%",
                        bottom: "100%",
                        transform: "translateX(-50%)",
                        marginBottom: "8px",
                    };
                    break;
                case "top-left":
                    styles = {
                        right: "100%",
                        bottom: "100%",
                        marginBottom: "8px",
                        marginRight: "8px",
                    };
                    break;
                case "top-right":
                    styles = {
                        left: "100%",
                        bottom: "100%",
                        marginBottom: "8px",
                        marginLeft: "8px",
                    };
                    break;
                case "bottom":
                    styles = {
                        left: "50%",
                        top: "100%",
                        transform: "translateX(-50%)",
                        marginTop: "8px",
                    };
                    break;
                case "bottom-left":
                    styles = {
                        right: "100%",
                        top: "100%",
                        marginTop: "8px",
                        marginRight: "8px",
                    };
                    break;
                case "bottom-right":
                    styles = {
                        left: "100%",
                        top: "100%",
                        marginTop: "8px",
                        marginLeft: "8px",
                    };
                    break;
                case "left":
                    styles = {
                        right: "100%",
                        top: "50%",
                        transform: "translateY(-50%)",
                        marginRight: "8px",
                    };
                    break;
                case "right":
                    styles = {
                        left: "100%",
                        top: "50%",
                        transform: "translateY(-50%)",
                        marginLeft: "8px",
                    };
                    break;
                default:
                    break;
            }

            const adjustedStyles = { ...styles };

            const tooltipLeft =
                wrapperRect.left +
                (styles.left === "50%"
                    ? wrapperRect.width / 2 - tooltipRect.width / 2
                    : 0);
            const tooltipRight = tooltipLeft + tooltipRect.width;
            const tooltipTop = wrapperRect.top - tooltipRect.height;
            const tooltipBottom = wrapperRect.bottom + tooltipRect.height;

            if (tooltipLeft < 0) {
                adjustedStyles.left = "0";
                adjustedStyles.transform = "none";
            } else if (tooltipRight > screenWidth) {
                adjustedStyles.right = "0";
                adjustedStyles.left = "auto";
                adjustedStyles.transform = "none";
            }

            if (tooltipTop < 0) {
                if (position.startsWith("top")) {
                    adjustedStyles.bottom = "auto";
                    adjustedStyles.top = "100%";
                    adjustedStyles.marginBottom = "0";
                    adjustedStyles.marginTop = "8px";
                }
            } else if (tooltipBottom > screenHeight) {
                if (position.startsWith("bottom")) {
                    adjustedStyles.top = "auto";
                    adjustedStyles.bottom = "100%";
                    adjustedStyles.marginTop = "0";
                    adjustedStyles.marginBottom = "8px";
                }
            }

            setTooltipStyles(adjustedStyles);
        }
    }, [visible, position]);

    return (
        <div
            className="relative inline-block"
            onMouseEnter={() => setVisible(true)}
            onMouseLeave={() => setVisible(false)}
            ref={wrapperRef}>
            {children}
            {visible && (
                <div
                    className="absolute z-10 w-max p-2 bg-neutral-800 text-white text-sm rounded shadow-lg"
                    style={tooltipStyles}
                    ref={tooltipRef}>
                    {content}
                </div>
            )}
        </div>
    );
};

export default Tooltip;
