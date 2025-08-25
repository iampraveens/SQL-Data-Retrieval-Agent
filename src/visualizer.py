from typing import List, Tuple, Optional
import matplotlib.pyplot as plt
import streamlit as st
import logging

logger = logging.getLogger(__name__)

def detect_plot_type(question: str) -> Optional[str]:
    """Detect plot type from question."""
    question_lower = question.lower()
    for p in ["bar", "pie", "line", "scatter"]:
        if p in question_lower:
            return p
    return None

def plot_results(columns: List[str], rows: List[Tuple], plot_type: str) -> Optional[plt.Figure]:
    """Plot the results using matplotlib."""
    if not rows:
        st.warning("No data to plot.")
        return None
    
    if len(columns) < 2:
        st.warning("Not enough columns for plotting.")
        return None
    
    data = list(zip(*rows))
    x = data[0]
    y = data[1]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if plot_type == "bar":
        ax.bar(x, y)
    elif plot_type == "pie":
        ax.pie(y, labels=x, autopct='%1.1f%%')
    elif plot_type == "line":
        ax.plot(x, y, marker='o')
    elif plot_type == "scatter":
        ax.scatter(x, y)
    else:
        st.warning(f"Unknown plot type: {plot_type}")
        return None
    
    ax.set_xlabel(columns[0])
    ax.set_ylabel(columns[1])
    ax.set_title(f"{plot_type.capitalize()} Plot: {columns[0]} vs {columns[1]}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return fig