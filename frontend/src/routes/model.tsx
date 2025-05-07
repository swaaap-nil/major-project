import { createFileRoute } from "@tanstack/react-router";
import Model from "../pages/Model";


export const Route = createFileRoute('/model')({
  component: Model,
});