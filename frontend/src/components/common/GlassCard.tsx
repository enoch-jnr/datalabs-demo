import { Card, CardProps } from "@mui/material";

export default function GlassCard(props: CardProps) {
  const { sx, children, ...rest } = props;
  return (
    <Card
      elevation={0}
      sx={{
        backdropFilter: "blur(16px)",
        backgroundColor: "rgba(255,255,255,0.72)",
        border: "1px solid rgba(255,255,255,0.5)",
        borderRadius: 4,
        ...sx,
      }}
      {...rest}
    >
      {children}
    </Card>
  );
}
