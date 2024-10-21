import type React from "react";
import styled from "styled-components";

const StyledContainer = styled.div`
    background: transparent;
    width: 100%;
    border-radius: 4px;
    border: 1x solid #c2c2c2;
    height: fit-content;
    padding: 20px;
`;

interface ContainerProps {
    children: React.ReactNode;
}

const Container: React.FC<ContainerProps> = ({ children }) => {
    return <StyledContainer>{children}</StyledContainer>;
};

export default Container;
